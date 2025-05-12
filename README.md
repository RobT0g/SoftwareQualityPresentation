# SoftwareQualityPresentation

The code on this repository is used to show examples of each of the 8 criteria for Software Quality as per the ISO/IEC 25000
The text below is written in portuguese becuase this is a presentation in my brazilian university 

# Exemplos dos critérios de qualidade de Software

## Aplicabilidade Funcional
Este critério se refere a capacidade do Software de atender a função para a qual foi criado. O exemplo para este critério se utiliza de um arquivo de biblioteca onde uma pessoa pode anotar todos os livros que ela leu.

O `bad_example.py` pode inicialmente parecer não conter problemas, mas acaba por gerar informações erradas diante de porblemas de formatação no arquivo da biblioteca, como linhas vazias ou comentários. Para resolver esses problemas, o `good_example.py` aplica algumas validações em cima do arquivo para ter uma acurácia maior.

## Eficiência/Performance
Este critério corresponde a capacidade do Sftware de ser eficiente em termos como tempo e uso de recursos. Para este exemplo, o sistema irá aplicar 2 formas de ordernar uma lista de números:
- `bad_example.py` aplica o Insert Sort; 
- `good_example.py` aplica o método nativo de sorting do python que corresponde ao Quick Sort.

A métrica neste caso é o tempo preciso para ordenar os números.

## Segurança
O critério da segurança é um dos mais relevantes hoje em dia. Para o exemplo, aqui existem 2 formas de manusear senhas a nível de software. A técnica mais segura, no exemplo do `good_example.py` utiliza uma técnica de hashing que é irreversível. Isso faz com que, mesmo tendo acesso ao banco de dados das senhas, não é possível acessar as senhas em si.

## Facilidade de manutenção e Confiabilidade (2 critérios)
Estes dois critérios foram capturados em um só exemplo para facilidade. A definição destes são:
- Facilidade de manutenção: O quão simples é de trabalhar com o código;
- Confiabilidade: O software é capaz de detectar e reagir a falhas? Está cobrindo todos os possíveis casos de uso?

Para isto, os dois exemplos fazem a mesma função sendo que o `good_example.py` emprega de uma forma que tem melhores métricas nestes critérios.
A função aqui é a de ler um aquivo txt que deveria ter uma formatação específica e gerar um report sobre estes.

## Compatibilidade e Portabilidade (2 critérios)
Este exemplo não é um código em si, mas será feito demonstrando as técnicas do Python para manusear dependencias e como isso pode ser feito em diversos sistemas operacionais. As definições dos critérios são:
- Compatibilidade: Pode rodar em vários SO diferentes;
- Portabilidade: O quão fácil é setar dependencias;

Para isso, a demonstração vai ser feita usando as funções do python de Virtual Environment

## Facilidade de uso
Aqui deu preguiça de fazer