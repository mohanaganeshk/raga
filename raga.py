import os
import chromadb
import numpy as np
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# Import the default embedding function from Chroma
from chromadb.utils import embedding_functions
from langchain_classic.evaluation import load_evaluator
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

DATA_PATH = "C:\\Users\\Viyan\\Exercism\\RAGa"

## Part ## 1: Data Loading
def load_documents():
    loader = DirectoryLoader(
        DATA_PATH, 
        glob="*.md", 
        loader_cls=TextLoader, 
        loader_kwargs={'encoding': 'utf-8'}
    )
    documents = loader.load()
    return documents

## Part ## 2: Data Splitting
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=500,
    length_function=len,
    add_start_index=True,
    )
chunks = text_splitter.split_documents(load_documents())

# Execute and validate each segment outputs
docs = load_documents()
print(f"Successfully loaded {len(docs)} documents.")
print(f"Split {len(docs)} documents into {len(chunks)} chunks.")
test_doc = chunks[10]; print(test_doc.page_content); print(test_doc.metadata)

## Part ## 3: Data Transformation
# Initialize your Chroma Client (Points to a local directory to save data permanently)
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Create or fetch your collection, Setting up & linking embedding function
collection = chroma_client.get_or_create_collection(
    name="my_markdown_collection",
    embedding_function=embedding_functions.DefaultEmbeddingFunction()
    # metadata={"hnsw:space": "cosine"} # <--- Forces Cosine Distance
)

# Extract text contents, IDs, and metadata from your LangChain chunks
documents_text = []
metadatas = []
ids = []

for index, chunk in enumerate(chunks):
    documents_text.append(chunk.page_content)
    
    # Chroma requires metadata values to be simple strings, integers, or floats
    metadatas.append({
        "source": str(chunk.metadata.get("source", "Unknown")),
        "start_index": int(chunk.metadata.get("start_index", 0))
    })
    
    # Every chunk must have a completely unique string ID
    ids.append(f"id_{index}")

# Add data directly to Chroma # Chroma automatically runs your text through 'default_ef' to create embeddings behind the scenes
collection.add(
    documents=documents_text,
    metadatas=metadatas,
    ids=ids
)

print(f"Successfully embedded and added {len(documents_text)} chunks to Chroma!")

# Print list all collections inside this database path & collection count
print(chroma_client.list_collections())

print(collection.count())


## Part ## 4: Querying Vector Database

# Generate vectors for two words using Chroma's default embedding model
word_1 = "eternity"
word_2 = "Horoscope"
word_3 = "Mr. Happy"
vector_1 = np.array(embedding_functions.DefaultEmbeddingFunction()([word_1]))
vector_2 = np.array(embedding_functions.DefaultEmbeddingFunction()([word_2]))
vector_3 = np.array(embedding_functions.DefaultEmbeddingFunction()([word_3]))

# Execute and validate each segment outputs
#<># print(f"Vector representation for '{word_1}': {vector_1}")
print(f"Vector count for '{word_1}': {len(vector_1)}")
#<># print(f"Vector count for '{word_2}': {len(vector_2)}")
#<># #print(f"Vector count for '{word_3}': {len(vector_3)}")

# Evaluate Cosine Similarity
cos_sim = cosine_similarity(vector_1, vector_2)[0][0]
cos_sim_2 = cosine_similarity(vector_1, vector_3)[0][0]

# Evaluate Euclidean Distance (L2)
euc_dist = euclidean_distances(vector_1, vector_2)[0][0]
euc_dist_2 = euclidean_distances(vector_1, vector_3)[0][0]

print(f"Cosine Similarity Score for {word_1} & {word_2}:  {cos_sim:.4f} # B/w  -1 and 1; 1.0 is identical and 0.0 is unrelated")
#<># print(f"Euclidean Distance Score for {word_1} & {word_2}: {euc_dist:.4f} # B/w 0 and infinity; 0.0 is identical and higher values are farther apart")
#<># print(f"Cosine Similarity Score for {word_1} & {word_3}: {cos_sim_2:.4f} # B/w  -1 and 1; 1.0 is identical and 0.0 is unrelated")
#<># print(f"Euclidean Distance Score for {word_1} & {word_3}: {euc_dist_2:.4f} # B/w 0 and infinity; 0.0 is identical and higher values are farther apart")

## Part ## 4: Querying Vector Database
# Search for a query in the database and return top_k results
def query_chroma(query_text, top_k=3, distance_threshold=0.7):
    results = collection.query(
        query_texts=[query_text],
        n_results=top_k
    )

    # ChromaDB returns nested lists inside a dictionary
    ids = results['ids'][0]
    documents = results['documents'][0]
    distances = results['distances'][0]
    metadatas = results['metadatas'][0]

    filtered_documents = []
    filtered_metadatas = []

    # Loop through all returned results to filter by distance threshold
    for i in range(len(distances)):
        # Default embedding uses L2 distance: lower is better, > 0.8 is usually irrelevant
        if distances[i] <= distance_threshold:
            filtered_documents.append(documents[i])
            filtered_metadatas.append(metadatas[i])

    if not filtered_documents:
        print(f"No relevant results found for: '{query_text}' (All distances exceeded {distance_threshold})")
        return None

    # Return only the relevant matches
    return {
        "documents": filtered_documents,
        "metadatas": filtered_metadatas
    }

#Question = "what is second filter"
Question_2 = "Minimum Spanning Tree"
search_results = query_chroma(Question_2, top_k=1, distance_threshold=0.7)
print(f"Search results for query: '{Question_2}': {search_results}")