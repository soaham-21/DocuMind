from duckduckgo_search import DDGS

def search_web(query, max_results=3):
    results=[]
    with DDGS() as ddgs:
        for result in ddgs.text(query, max_results=max_results):
            results.append(result["body"])

        if not results:
            return ["no web results found"]
        return results

def answer_from_web(query, chunks):
    context = ""
    for i, chunk in enumerate(chunks):
        context += f"[Web Result {i+1}]:\n{chunk}\n\n"
    
    return context