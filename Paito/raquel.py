#gera tabelas para impressao

html='''
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
  text-align:center;
  border: 1px solid black;
  border-collapse: collapse;
}
  #xd{
    padding-top:0px;
    border-bottom: 1px solid white;
    border-collapse: collapse;
  }
  #nr{
    border-bottom: 1px solid white;
    border-collapse: collapse;
  }
</style>
</head>
<body>

<table style="width:100%">
  <tr>
    <td style="width:15%">N° $var </td>
    <td id="xd">Ano Turma</td>
    <td>Nome do Aluno<pre>
    
    </pre></td>
    <td id="xd">Escola Origem</td>
    <td id="nr">Assinatura do </br>Responsável</td>
  </tr>
  <tr>
    <td><pre></pre>Data</br>___/___/2020</td>
    <td></td>
    <td>Nome do Responsável<pre>
    
    </pre></td>
    <td></td>
    <td></td>
  </tr>
 
</table>
</br>
$parte
</body>
</html>
'''

parte = '''
</br>
</br>
</br>
</br>
<table style="width:100%">
  <tr>
    <td style="width:15%">N° $var </td>
    <td id="xd">Ano Turma</td>
    <td>Nome do Aluno<pre>
    
    </pre></td>
    <td id="xd">Escola Origem</td>
    <td id="nr">Assinatura do </br>Responsável</td>
  </tr>
  <tr>
    <td><pre></pre>Data</br>___/___/2020</td>
    <td></td>
    <td>Nome do Responsável<pre>
    
    </pre></td>
    <td></td>
    <td></td>
  </tr>
  
</table>
</br>
$parte'''

h = html
cont = 0
pag = 1
for k in range(898, 1053):
  h = h.replace('$var', str(k))
  cont+=1 
  if cont == 5:
    h = h.replace('$parte', str(pag)+parte)
    pag+=1
    cont = 0
  else:
    h = h.replace('$parte', parte) 
    
h = h.replace('$var', str(k))
h = h.replace('$parte','')
print(h)
