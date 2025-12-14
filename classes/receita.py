from pydantic import BaseModel
import google.generativeai as gemini_ai
import os 
from dotenv import load_dotenv 
load_dotenv() 
 
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gemini_ai.configure(api_key=GOOGLE_API_KEY)
model = gemini_ai.GenerativeModel('gemini-2.5-flash') 

class Receita(BaseModel):
    ingredientes: str
    porcoes: int
    restricao: str | None = None
    user_id: int
    
    def gerar(self):
        prompt = f"""
        Gere uma receita usando apenas os ingredientes: {self.ingredientes}.
        Sirva {self.porcoes} porções.
        Evite as restrições: {self.restricao or 'nenhuma'}.
        Não envie a mensagem "com certeza" por favor!
        """
        return model.generate_content(prompt), prompt
