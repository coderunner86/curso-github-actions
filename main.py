import os 

def main():
    nombre = os.getenv("USERNAME")
    print(f'Hola, {nombre} Github Actions')

if __name__ == "__main__":
    main()
