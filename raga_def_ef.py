import sys
import chromadb
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from chromadb.utils import embedding_functions

DATA_PATH = "C:\\Users\\Viyan\\Exercism\\RAGa"

PROMPT_TEMPLATE = """
You are a technical document assistant reviewing a markdown file. 
Analyze the provided background facts and answer the question naturally.

Background Facts:
{context}

Question: {question}
Helpful Answer:
"""


print(f"Stage 1: Data Loading - Loading documents from: {DATA_PATH}")
def load_documents():
    loader = DirectoryLoader(
        DATA_PATH, 
        glob="*.md", 
        loader_cls=TextLoader, 
        loader_kwargs={'encoding': 'utf-8'}
    )
    documents = loader.load()
    return documents
docs = load_documents()
print(f"\tSuccessfully split {len(docs)} documents.")

print("Stage 2: Data Splitting - Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=50,
    separators=["\n\n", "\n", " ", ""]
    )
chunks = text_splitter.split_documents(docs)
print(f"\tSuccessfully split {len(docs)} documents into {len(chunks)} chunks.")

print("Stage 3: Data Transformation - Initializing ChromaDB and embedding function...")
chroma_client = chromadb.PersistentClient(path="./chroma_db")
ef = embedding_functions.DefaultEmbeddingFunction()

collection = chroma_client.get_or_create_collection(
    name="my_markdown_collection",
    embedding_function=ef,
    metadata={"hnsw:space": "cosine"}
)

print(f"\tPopulating ChromaDB with chunks...")
if collection.count() > 0:
    print("\tDatabase already populated. Reusing existing collection data.")
else:
    print("\tDatabase is empty. Processing files...")
collection.add(
    documents=[doc.page_content for doc in chunks],
    metadatas=[doc.metadata for doc in chunks],
    ids=[f"{doc.metadata.get('source', 'chunk')}_{i}" for i, doc in enumerate(chunks)]
)

print("Stage 5: Querying Vector DB: Querying ChromaDB for relevant context...")
def query_chroma(query_text, top_k=3, distance_threshold=0.5):
    results = collection.query(
        query_texts=[query_text],
        n_results=top_k
    )

    if not results or not results['documents'] or not results['documents'][0]:
        print(f"No results found for: '{query_text}'")
        return None

    documents = results['documents'][0]
    distances = results['distances'][0]
    metadatas = results['metadatas'][0]

    filtered_documents = []
    filtered_metadatas = []

    for i in range(len(distances)):
        if distances[i] <= distance_threshold:
            filtered_documents.append(documents[i])
            filtered_metadatas.append(metadatas[i])

    if not filtered_documents:
        print(f"No relevant results found for: '{query_text}' (All distances exceeded {distance_threshold})")
        return None

    return {
        "documents": filtered_documents,
        "metadatas": filtered_metadatas
    }

if len(sys.argv) > 1:
    Question = sys.argv[1]
    print(f"\tProcessing your question: '{Question}'")
else:
    Question = input("Ask a question: ")

search_results = query_chroma(Question)
#<># print(f"\tSearch results for query: '{Question}': \n {search_results}")

print("Stage 6: Building context for LLM prompt...")
if search_results and "documents" in search_results and search_results["documents"]:
    context_text = "\n\n".join(search_results["documents"])
else:
    context_text = "No relevant context found in the local knowledge base."

#<># print(f"\t\nContext Text to LLM: \n{context_text}")

print("Stage 7: Generating response using LLM...")
prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
prompt = prompt_template.format(context=context_text, question=Question)
#<># print(f"\t\n Prompt to LLM: {prompt}")

print(f"\tInitialize model and invoke LLM with the formatted prompt")
llm = ChatOllama(model="llama3.2:1b", temperature=0)
response = llm.invoke(prompt)
print("\tLLM Final Answer:")
print(response.content)