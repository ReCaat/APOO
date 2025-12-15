from Interface import ControleDeAcessos

def main():
    controller = ControleDeAcessos()

    while(True):
        exit = controller.interfaceInicial()
        if(exit):
            return
        
        controller.areaUsuario()

    print("Sistema fechado com sucesso\n")

if __name__=="__main__":
    main()