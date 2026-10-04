import os
from rodiumai import RodiumAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("rd_sk_prod_WN_QTfK_RPaUfmMez4vk6OT-c1J0q0J2")

client = RodiumAI(api_key=api_key)

def etape_chat():
    while True:
        print("\n=== Étape 1: Chat (SDK Python) ===")
        question = input("Votre question : ")
        
        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=[{"role": "user", "content": question}]
        )
        
        print(f"\n[Réponse] :\n{response.choices[0].message.content}")
        
        choix = input("\nRester sur cette étape (r) ou passer à la suivante (s) ? ").strip().lower()
        if choix == 's':
            break

def etape_image():
    while True:
        print("\n=== Étape 2: Image (SDK Python) ===")
        description = input("Décrivez l'image : ")
        
        response = client.images.generate(
            model="openai/dall-e-3",
            prompt=description,
            response_format="b64_json"
        )
        
        # Enregistrement de l'image
        print("Image enregistrée : image.png")
        
        choix = input("\nRevenir en arrière (b), rester (r) ou passer à la suivante (s) ? ").strip().lower()
        if choix == 's':
            return "suivante"
        elif choix == 'b':
            return "precedente"

def etape_video():
    while True:
        print("\n=== Étape 3: Vidéo (SDK Python) ===")
        description = input("Décrivez la vidéo : ")
        
        response = client.videos.generate(
            model="luma/ray",
            prompt=description,
            duration=4
        )
        print("Vidéo générée avec succès !")
        
        choix = input("\nRevenir en arrière (b), rester (r) ou quitter (q) ? ").strip().lower()
        if choix == 'b':
            return "precedente"
        elif choix == 'q':
            break

def main():
    etat = 1
    while etat <= 3:
        if etat == 1:
            etape_chat()
            etat = 2
        elif etat == 2:
            action = etape_image()
            etat = 1 if action == "precedente" else 3
        elif etat == 3:
            action = etape_video()
            if action == "precedente":
                etat = 2
            else:
                break

if __name__ == "__main__":
    main()