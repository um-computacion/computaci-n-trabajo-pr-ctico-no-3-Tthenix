from exceptions import ingrese_numero, NumeroDebeSerPositivo

def main():    
    while True:
        try:
            numero = ingrese_numero()
            print(f"Número válido: {numero}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
        except NumeroDebeSerPositivo as e:
            print(f"Error: {e}\n")
        except KeyboardInterrupt:
            print("\nPrograma finalizado.")
            break

if __name__ == "__main__":
    main()