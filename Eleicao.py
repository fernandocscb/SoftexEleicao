'''Desenvolva um código que simule uma eleição com três candidatos.
- candidato_X => 889
- candidato_Y => 847
- candidato_Z => 515
- branco => 0
O código deve perguntar se deseja finalizar a votação depois do voto.
Caso o número do voto não corresponda a nenhum candidato ou seja branco, 
ele deve ser tratado como nulo. Se for inserido um texto ao invés de número, 
o código deve retornar uma mensagem para votar novamente.
Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele 
com o maior número de votos e, também, a quantidade de votos de cada candidato, 
os brancos e nulos 
'''

finalizar = ''
cand_X = 0 
cand_Y = 0 
cand_Z = 0 
nulos = 0

def votacao(voto):
    global cand_X, cand_Y, cand_Z, nulos
    if(voto == 889):
        cand_X += 1
    elif( voto == 847):
        cand_Y += 1 
    elif (voto == 515):
        cand_Z += 1 
    else:
        nulos += 1 
def resultado():
    global ordenou
    if(cand_X > cand_Y and cand_X > cand_Z):
        print('vencedor: candidato_X' )
        print('votos: ' + str(cand_X))
        print('Votos candidato_Y: '+ str(cand_Y))
        print('Votos candidato_Z: ' + str(cand_Z))
    elif(cand_Y > cand_Z and cand_Y > cand_X):
        print('vencedor: candidato_Y' )
        print('votos: ' +str( cand_Y))
        print('Votos candidato_X: '+ str(cand_X))
        print('Votos candidato_Z: ' + str(cand_Z))
    elif(cand_Z > cand_X and cand_Z > cand_Y):
        print('vencedor: candidato_Z' )
        print('votos: ' + str(cand_Z))
        print('Votos candidato_Y: '+ str(cand_Y))
        print('Votos candidato_X: ' + str(cand_X))
    else:
        print('Empate')
        print('votos candidato_Z: ' + str(cand_Z))
        print('Votos candidato_Y: '+ str(cand_Y))
        print('Votos candidato_X: ' + str(cand_X))
     
while(finalizar != 's'):
        try:
            voto = float(input('Digite seu voto: '))
            votacao(voto)
            finalizar = input('Deseja finalizar votação? S  /  N ?')
        except:
            print('Só números são aceitos')
resultado()
print('Votos nulos: ' + str(nulos))