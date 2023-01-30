import requests, os, time
from pystyle import Colorate, Colors, Center


status = [200, 201, 204]


token = input(Colorate.Horizontal(Colors.blue_to_cyan, "[?] Token >>> "))

os.system("clear")
print(
        Colorate.Horizontal(
            Colors.blue_to_cyan,
            Center.XCenter(
                """
                
        ╦ ╦╦ ╦╔═╗╦═╗╔═╗  ╔═╗╔╦╗╔═╗╔╦╗╦ ╦╔═╗
        ╠═╣╚╦╝╠═╝╠╦╝║╣   ╚═╗ ║ ╠═╣ ║ ║ ║╚═╗
        ╩ ╩ ╩ ╩  ╩╚═╚═╝  ╚═╝ ╩ ╩ ╩ ╩ ╚═╝╚═╝
        
                 [+] Dev : Hypre#9999
        
        
        
        """
        ),
        
     )
  
  )

headers = {"authorization": token}

def about_changer():
      print()

      about = input(Colorate.Horizontal(Colors.blue_to_cyan, "[?] About  >>> "))
      data = {"bio": about}

      r = requests.patch("https://discord.com/api/v9/users/%40me/profile", json=data, headers=headers)

      if r.status_code in status:
        os.system("clear")
        print(
        Colorate.Horizontal(
            Colors.blue_to_cyan,
            Center.XCenter(
                f"""
                [SUCCESS] About Changed To: {about}
                
                """
                ),
              
              )
           
           )
      else:

        os.system("clear")
        print(
        Colorate.Horizontal(
            Colors.blue_to_cyan,
            Center.XCenter(
                f"""
                [FAILED] About Changed To: {about}
                
                """
                ),
              
              )
           
           )
      time.sleep(1.5)
 

about_changer()
