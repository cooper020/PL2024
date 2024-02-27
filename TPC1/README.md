
# PL2024

## TPC1

**Nome:** Henrique Morais Pereira

**ID:** A100831

**Enunciado:**
O objetivo é ler e analisar um conjunto de dados, a partir do qual se pretende extrair várias informações. Primeiro, pretende-se obter uma lista das diferentes modalidades desportivas presentes no conjunto de dados, ordenadas alfabeticamente. Em seguida, obter o cálculo as percentagens de atletas que estão aptos e inaptos para a prática desportiva. Por fim, é necessário distribuir os atletas por diferentes escalões etários, onde cada escalão representa um intervalo de 5 anos, como [30-34], [35-39], e assim por diante. 

**Descrição:**
Está definida uma função chamada process_data. Esta função é responsável por processar os dados do dataset, começa por inicializar várias listas vazias e variáveis que serão usadas para armazenar e contar informações à medida que os dados são processados.

A função entra num loop onde lê cada linha do dataset. A primeira linha é ignorada, visto que é o cabeçalho do dataset. Para cada linha subsequente, a função divide a linha em elementos separados por vírgulas e processa esses elementos.

Se a modalidade  ainda não estiver na lista, ela é adicionada. O número total de atletas é incrementado para cada linha. Se o atleta está apto para a prática desportiva ), o contador de atletas aptos é incrementado, caso contrário, o contador de atletas inaptos é incrementado.

Dependendo da idade do atleta, o atleta é adicionado à lista correspondente ao seu escalão etário. Os escalões etários são definidos por intervalos de 5 anos. Depois de todas as linhas serem processadas, a lista de modalidades é ordenada alfabeticamente e a função retorna todas as listas e contadores que foram preenchidos durante o processamento.
A função print_results recebe todas as listas e os contadores retornados pela função process_data e imprime os resultados. Ela calcula as percentagens de atletas aptos e inaptos, bem como a distribuição de atletas por escalão etário. Estes resultados são então impressos.

