import ipaddress

def analyse_reseau(reseau):

    try:
        ip = ipaddress.ip_network(reseau)
    except:
        print("réseau invalide")
        quit()

    list_ip = list(ip.hosts())

    print(f"Masque: {ip.netmask}")
    print(f"Nombre d'adresses disponible: {ip.num_addresses}")
    print(f"Première adresse: {list_ip[0]}")
    print(f"Dernière adresse: {list_ip[-1]}")
    print(f"Adresse de diffusion: {ip.broadcast_address}")


def find_reseau(ip):

    interface = ipaddress.ip_interface(ip)
    reseau = interface.network

    return reseau

def check_ip(ip):
    if not "/" in ip:
        print("Le masque n'a pas été rentré")
        return False
    return True

def enter_ip():
    ip = input("Rentrer une adresse: ")
    return ip

def enter_reseau():
    reseau = input("Rentrer un adresse: ")
    return reseau

def check_reseau(reseau):
    if not "/" in reseau:
        print("Adresse invalide")

    try:
        reseau = ipaddress.ip_network(reseau)
    except:
        print("adresse invalide")
        return False
    return True



def main():
    print("[0] Adresse IP")
    print("[1] Adresse réseau")
    choix = int(input("Que souhaitez vous rentrer: "))
    if choix == 0:

        while True:
            ip = enter_ip()
            if check_ip(ip):
                break

        reseau = find_reseau(ip)
        print("---")
        print(analyse_reseau(reseau))
        print("---")

    elif choix == 1:
        while True:
            reseau = enter_reseau()
            if check_reseau(reseau):
                break
        print("---")
        print(analyse_reseau(reseau))
        print("---")



if __name__ == "__main__":
    main()
