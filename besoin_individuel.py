from numpy import *
from pandas import *
from openpyxl import *
import streamlit as st
def saut_ligne(i):
    for i in range(int(i)):
        st.write("")
    return

def main():
    st.write('<img class="Logo-etat" src="https://www.inrae.fr/themes/custom/inrae_socle/public/images/etat_logo.svg" alt="République française" width="138" height="146">',
             '<img class="Logo-site" src="https://www.inrae.fr/themes/custom/inrae_socle/logo.svg" alt="INRAE">',
             unsafe_allow_html=True)
    st.header(":blue[INRAE Besoins individuels]")
    uploaded_file = st.file_uploader("Téléversez un fichier Excel", type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            # Lecture du fichier Excel avec Pandas
            classeur = load_workbook(uploaded_file)
            wb = classeur.sheetnames
            wa = wb[1]
            drap = classeur[wa]

            # Extraction des données pour les pôles
            L = []
            for i in drap["N"]:
                L.append(str(i.value))
            L.pop(0)
            L.pop(0)
            L.pop(0)
            L.sort()
            Lp = unique([x for x in L if x and x != "None"])

            # Extraction des données pour les agents
            agent = []
            for row in drap.iter_rows(min_row=4, values_only=True):
                nom = row[3]
                prenom = row[4]
                if nom and prenom:
                    nom_prenom = f"{nom} {prenom}"
                    if nom_prenom.strip():
                        agent.append(nom_prenom.strip())
            La = agent

            # Extraction des données complètes
            data = []
            for i, row in enumerate(drap.iter_rows(values_only=True), start=1):
                if i == 2:  # Exclure la deuxième ligne (titres)
                    continue
                nom = row[3]
                prenom = row[4]
                if nom and prenom:
                    nom_prenom = f"{nom} {prenom}"
                    data_row = list(row)
                    data_row[3] = nom_prenom
                    del data_row[4]
                    data.append(data_row)

            # Trier les données par ordre alphabétique du nom de famille
            data.sort(key=lambda x: x[3] if x[3] is not None else "")

            # Organiser les données en fonction des pôles
            data_organized = []
            for i in range(len(Lp)):
                L1 = []
                for j in range(len(data)):
                    if data[j][-1] == Lp[i]:
                        L1.append(data[j])
                data_organized.append(L1)

            selected_pole = st.selectbox("Choisissez un pôle", Lp)

            # Filtrer les données correspondantes au pôle sélectionné
            filtered_data = [row for row in data if row[-1] == selected_pole]

            # Créer le menu déroulant pour choisir un agent parmi le pôle sélectionné
            selected_agent = st.selectbox("Choisissez un agent", [row[3] for row in filtered_data])

            # Filtrer les données correspondantes à l'agent sélectionné
            filtered_data_agent = [row for row in filtered_data if row[3] == selected_agent]

            # Créer le DataFrame avec les données filtrées pour le premier tableau
            df = DataFrame(filtered_data_agent)
            header = [cell.value for cell in drap[2]]
            header = header[:len(df.columns)]
            df.columns = header
            st.dataframe(df, use_container_width=False, height=140, hide_index=True)
            st.column_config.TextColumn(width="small")

            saut_ligne(5)

            # Créer le DataFrame avec les données filtrées pour le deuxième tableau
            df3 = DataFrame(filtered_data)
            header = [cell.value for cell in drap[2]]
            header = header[:len(df3.columns)]
            df3.columns = header
            st.dataframe(df3, use_container_width=True, height=400, hide_index=True)
            st.column_config.TextColumn(width="small")
        
        except UnboundLocalError:
            # Afficher "Hello World" en cas d'erreur
            st.write("Hello World")
    return
'''''
def main1():
    #st.header(":blue[INRAE BPP]")
    Lp_dico = {}
    z = 0
    for i in Lp:
        Lp_dico[i] = z
        z += 1
    option = st.selectbox("CHOISISSEZ LE SCIENTIFIQUE ⬇️",Lp)
    g = Lp_dico[option]
    st.title(Lp[g])
    La_dico = {}
    z = 0
    for i in La:
        La_dico[i] = z
        z += 1
    option = st.selectbox("CHOISISSEZ LE SCIENTIFIQUE ⬇️",La)
    m = La_dico[option]
    st.title(La[m])
    #print(Sc_data)
    df = DataFrame(Sc_data[m])
    df.columns=Headers
    st.dataframe(df, use_container_width= True, height= 400, hide_index= True)
    st.column_config.TextColumn(width="small")
    return
#scientifique()
#print(df)
#print(len(Sc_data))

#REPARTIR LA DATA POUR CHAQUE LIGNE ANALYTIQUE
K = []
L = []
Z = []
for i in range(len(La)):
    K.append(L)
#print(K)
J = []
w = 0
#print(Sc_data_final)
for i in range(len(La)): 
    L = []
    e = 0
    for k in range(len(Sc_data_final)):
        if str(Sc_data_final[k][10]) == str(La[i]):
            #K[i].append(Sc_data_final[k])
            L.append(e)
            #print(Sc_data_final[e][6])   #pass      
        e += 1
    for j in L:
        #print(j)
        J.append(str(Sc_data_final[int(j)]))
    Z.append(J)
    L = []
    J = []
#print(Z[1])
L1, L2, L3 = [], [], []
for i in range(len(Z)): 
    L2 = []
    for j in Z[i]:
        L1 = []
        #print(j)
        r = ''
        split2 = j.split("', '")
        for z in range(2, len(split2[0])):
            r += split2[0][z]
        split2[0] = r    
        r = ''
        for z in range(len(split2[len(split2)-1])-2):
            r += split2[len(split2)-1][z]
        split2[len(split2)-1] = r
        #print(split2)
        for k in split2:
            #print(k)
            #print(k)
            L1.append(k)
        L2.append(L1)
    L3.append(L2)
#print(L3[0][0][0])


La_data = L3
#print(L3[3])
unique_data = []
seen = set()
for scientist_data in La_data:
    unique_scientist_data = []
    for row in scientist_data:
        if tuple(row) not in seen:
            seen.add(tuple(row))
            unique_scientist_data.append(row)
    unique_data.append(unique_scientist_data)

La_data = unique_data
#print(La_data)

#METTRE EN FORME AVEC STREAMLIT ANALYTIQUE
def analytique():
    #st.header(":blue[INRAE BPP]")
    La_dico = {}
    z = 0
    for i in La:
        La_dico[i] = z
        z += 1
    option = st.selectbox("CHOISISSEZ LA LIGNE ANALYTIQUE ⬇️",La)
    m = La_dico[option]
    a = "Code :  " + str(La[m]) 
    st.title(a)
    df = DataFrame(La_data[m])
    df.columns=Headers
    st.dataframe(df, use_container_width= True, height=700, hide_index=True)
    st.column_config.TextColumn(width="small")
    return
#analytique()
#print(df)
#print(len(Sc_data))
















#GET LES CHIFFRES CLES

budg = 0
for i in range(len(Sc_data_final)):
    budg = budg + float(Sc_data_final[i][12])
budget = round(budg, 2)

dep = 0
for i in range(len(Sc_data_final)):
    dep = dep + float(Sc_data_final[i][13])
depense = round(dep, 2)


budg_d = 0
#print(Sc_data_final[len(Sc_data_final)-2][15])
for i in range(len(Sc_data_final)):
    #print(Sc_data)
    budg_d = budg_d + float(Sc_data_final[i][15])
budget_disponible = round(budg_d, 2)

nombre_mission = len(Sc_data_final)+1


Table_final = []
for i in range(len(Sc_data)):
    for j in range(len(Sc_data[i])):
        Table_final.append(Sc_data[i][j])



#METTRE L ENSEMBLE DU DATAFRAME
def table_complete():
    df = DataFrame(Table_final)
    df.columns=Headers
    #st.markdown(' ')
    st.dataframe(data=df, use_container_width= True, height=700)
    st.column_config.TextColumn(width="small")
    return 
#table_complete()

#FONCTIONS PRATIQUE STREMLIT
def saut_ligne(i):
    for i in range(int(i)):
        st.write("")
    return













def scientifique_drap(drap):
    L = []
    for i in drap["H"]:
        L.append(i.value)
    L.pop(0)
    L.sort()
    Sc = array(L).unique()


#Get toute la data
    a = ''
    for line in drap:
        for i in line:
        #print(str(i.value))
            a =  a + "{" + str(i.value)

#Split la data
    Sc_data = []
    Sc_data_final = []
    Sc_data.append(a.split("BPP"))
    V = Sc_data[0][0]
    Sc_data[0].pop(0)
#print(Sc_data[0][1])
    for j in range(len(Sc_data[0])-1):
        A = []
        a = ''
        a = str(Sc_data[0][j])
        split1 = a.split('{')
    #print(split1)
        for i in split1:
            A.append(i)
        A.pop(0)
        A.pop(len(split1)-2)
    #print(A)
        Sc_data_final.append(A)
    a = ''
    a = str(Sc_data[0][len(Sc_data)-2])
    split1 = a.split('{')
#print(str(Sc_data[0][len(Sc_data)-2]))
#print(len(Sc_data[0]))
    A = []
    for i in split1:
        A.append(i)
    A.pop(0)
#print(A)
    Sc_data_final.append(A)
#print(Sc_data_final[100:400])
#for k in range(len(Sc_data_final)):
    #print(Sc_data_final[k])

#Répartir la data pour chaque scientifique
    K = []
    L = []
    Z = []  
    for i in range(len(Sc)):
        K.append(L)
#print(K)
    J = []
    w = 0
    for i in range(len(Sc)): #len(Sc)
        L = []
        e = 0
        for k in range(len(Sc_data_final)):
            if str(Sc_data_final[k][6]) == str(Sc[i]):
            #K[i].append(Sc_data_final[k])
                L.append(e)
            #print(Sc_data_final[e][6])   #pass      
            e += 1
        for j in L:
        #print(j)
            J.append(str(Sc_data_final[int(j)]))
        Z.append(J)
        L = []
        J = []
#print(Z[7:20])
    L1, L2, L3 = [], [], []
    for i in range(len(Z)): 
        L2 = []
        for j in Z[i]:
            L1 = []
        #print(j)
            r = ''
            split2 = j.split("', '")
            for z in range(2, len(split2[0])):
                r += split2[0][z]
            split2[0] = r    
            r = ''
            for z in range(len(split2[len(split2)-1])-2):
                r += split2[len(split2)-1][z]
            split2[len(split2)-1] = r
        #print(split2)
            for k in split2:
            #print(k)
            #print(k)
                L1.append(k)
            L2.append(L1)
        L3.append(L2)
#print(L3[0][0][0])
    Sc_data = L3
    L2 = []
    for i in range(len(Sc_data)):
        L = []
        for j in range(len(Sc_data[i])):
            L.append(Sc_data[i][j][16])
        M = []
        for r in L:
            a = str(r)
            split1 = a.split(" ")[0]
            M.append(split1)
        #print(M)
        D = M.copy()
        M.sort()
        L1 = []
        #print(D)
        #print(M)
        for z in range(len(M)):
            for l in range(len(D)):
                if M[z] == D[l]:
                    Sc_data[i][l][16] = M[z]
                    L1.append(Sc_data[i][l])
    #print(L1)        
        L2.append(L1)
    Sc_data = L2

#MISE EN FORME DES EN-TETES
    Headers = []
    b = str(V)
    split = b.split("{")
    for i in split:
        Headers.append(i)
    Headers.pop(0)
    Headers.pop(0)
    Headers.pop(len(Headers)-1)
#print(Headers)

    Headers_d = {}
    z = 0
    for i in Headers:
        Headers_d[z] = i
        z += 1

    Sc_dico = {}
    z = 0
    for i in Sc:
        Sc_dico[i] = z
        z += 1
    option = st.selectbox("CHOISISSEZ LE SCIENTIFIQUE ⬇️",Sc)
    m = Sc_dico[option]
    st.title(Sc[m])
    df = DataFrame(Sc_data[m])
    df.columns=Headers
    st.dataframe(df, use_container_width= True, height= 400, hide_index= True)
    st.column_config.TextColumn(width="small")
    
    return


def analytique_drap(drap):
    L = []
    for i in drap["H"]:
        L.append(i.value)
    L.pop(0)
    L.sort()
    Sc = array(L).unique()

    L = []
    for i in drap["L"]:
        L.append(i.value)
    L.pop(0)
    L.sort()
    La = array(L).unique()

#Get toute la data
    a = ''
    for line in drap:
        for i in line:
        #print(str(i.value))
            a =  a + "{" + str(i.value)

#Split la data
    Sc_data = []
    Sc_data_final = []
    Sc_data.append(a.split("BPP"))
    V = Sc_data[0][0]
    Sc_data[0].pop(0)
#print(Sc_data[0][1])
    for j in range(len(Sc_data[0])-1):
        A = []
        a = ''
        a = str(Sc_data[0][j])
        split1 = a.split('{')
    #print(split1)
        for i in split1:
            A.append(i)
        A.pop(0)
        A.pop(len(split1)-2)
    #print(A)
        Sc_data_final.append(A)
    a = ''
    a = str(Sc_data[0][len(Sc_data)-2])
    split1 = a.split('{')
#print(str(Sc_data[0][len(Sc_data)-2]))
#print(len(Sc_data[0]))
    A = []
    for i in split1:
        A.append(i)
    A.pop(0)
#print(A)
    Sc_data_final.append(A)
#print(Sc_data_final[100:400])
#for k in range(len(Sc_data_final)):
    #print(Sc_data_final[k])

#Répartir la data pour chaque scientifique
    
#MISE EN FORME DES EN-TETES
    Headers = []
    b = str(V)
    split = b.split("{")
    for i in split:
        Headers.append(i)
    Headers.pop(0)
    Headers.pop(0)
    Headers.pop(len(Headers)-1)
#print(Headers)

    Headers_d = {}
    z = 0
    for i in Headers:
        Headers_d[z] = i
        z += 1
    K = []
    L = []
    Z = []
    for i in range(len(La)):
        K.append(L)
#print(K)
    J = []
    w = 0
#print(Sc_data_final)
    for i in range(len(La)): 
        L = []
        e = 0
        for k in range(len(Sc_data_final)):
            if str(Sc_data_final[k][10]) == str(La[i]):
            #K[i].append(Sc_data_final[k])
                L.append(e)
            #print(Sc_data_final[e][6])   #pass      
            e += 1
        for j in L:
        #print(j)
            J.append(str(Sc_data_final[int(j)]))
        Z.append(J)
        L = []
        J = []
#print(Z[1])
    L1, L2, L3 = [], [], []
    for i in range(len(Z)): 
        L2 = []
        for j in Z[i]:
            L1 = []
        #print(j)
            r = ''
            split2 = j.split("', '")
            for z in range(2, len(split2[0])):
                r += split2[0][z]
            split2[0] = r    
            r = ''
            for z in range(len(split2[len(split2)-1])-2):
                r += split2[len(split2)-1][z]
            split2[len(split2)-1] = r
        #print(split2)
            for k in split2:
            #print(k)
            #print(k)
                L1.append(k)
            L2.append(L1)
        L3.append(L2)
#print(L3[0][0][0])

    Sc_data = L3
    L2 = []
    for i in range(len(Sc_data)):
        L = []
        for j in range(len(Sc_data[i])):
            L.append(Sc_data[i][j][16])
        M = []
        for r in L:
            a = str(r)
            split1 = a.split(" ")[0]
            M.append(split1)
        #print(M)
        D = M.copy()
        M.sort()
        L1 = []
        #print(D)
        #print(M)
        for z in range(len(M)):
            for l in range(len(D)):
                if M[z] == D[l]:
                    Sc_data[i][l][16] = M[z]
                    L1.append(Sc_data[i][l])
    #print(L1)        
        L2.append(L1)
    Sc_data = L2
#print(L3[3])

#METTRE EN FORME AVEC STREAMLIT ANALYTIQUE
    #st.header(":blue[INRAE BPP]")
    La_dico = {}
    z = 0
    for i in La:
        La_dico[i] = z
        z += 1
    option = st.selectbox("CHOISISSEZ LA LIGNE ANALYTIQUE ⬇️",La)
    m = La_dico[option]
    a = "Code :  " + str(La[m]) 
    st.title(a)
    df = DataFrame(Sc_data[m])
    df.columns=Headers
    st.dataframe(df, use_container_width= True, height=700, hide_index=True)
    st.column_config.TextColumn(width="small")
    
    return


def table_drap(drap):
    L = []
    for i in drap["H"]:
        L.append(i.value)
    L.pop(0)
    L.sort()
    Sc = array(L).unique()


#Get toute la data
    a = ''
    for line in drap:
        for i in line:
        #print(str(i.value))
            a =  a + "{" + str(i.value)

#Split la data
    Sc_data = []
    Sc_data_final = []
    Sc_data.append(a.split("BPP"))
    V = Sc_data[0][0]
    Sc_data[0].pop(0)
#print(Sc_data[0][1])
    for j in range(len(Sc_data[0])-1):
        A = []
        a = ''
        a = str(Sc_data[0][j])
        split1 = a.split('{')
    #print(split1)
        for i in split1:
            A.append(i)
        A.pop(0)
        A.pop(len(split1)-2)
    #print(A)
        Sc_data_final.append(A)
    a = ''
    a = str(Sc_data[0][len(Sc_data)-2])
    split1 = a.split('{')
#print(str(Sc_data[0][len(Sc_data)-2]))
#print(len(Sc_data[0]))
    A = []
    for i in split1:
        A.append(i)
    A.pop(0)
#print(A)
    Sc_data_final.append(A)
    for i in range(len(Sc_data_final)):
        Sc_data_final[i][16] = 1
    Headers = []
    b = str(V)
    split = b.split("{")
    for i in split: 
        Headers.append(i)
    Headers.pop(0)
    Headers.pop(0)
    Headers.pop(len(Headers)-1)
#print(Headers)
    Headers_d = {}
    z = 0
    for i in Headers:
        Headers_d[z] = i
        z += 1
    df = DataFrame(Sc_data_final)
    df.columns=Headers
    #st.markdown(' ')
    st.dataframe(data=df, use_container_width= True, height=700)
    st.column_config.TextColumn(width="small")
    return

'''''