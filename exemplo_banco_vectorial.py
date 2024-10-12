import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="lustore")

collection.add(
    documents=[
        "A Lustore vai abrir loja física em Angola",
        "A Lustore vai abrir loja física em Namibia",
        "A Lustore vai abrir loja física em África do Sul",
        "A Lustore vai abrir loja física na Zambia",
        "A Lustore vai abrir loja física em Moçambique",
        "A Lustore vai abrir loja física no Congo",
        "A Lustore vai abrir loja física no Brasil",
        "A Lustore vai abrir loja física em Portugal",
        "A Lustore vai abrir loja física em Cabo Verde"
    ],
    ids=["pais1", "pais2", "pais3", "pais4", "pais5", "pais6", "pais7", "pais8", "pais9", "pais9"]
)

resultado = collection.query(
    query_texts=["A Lustore vai ter loja em Luanda?"],
    n_results=3
)

print(resultado)