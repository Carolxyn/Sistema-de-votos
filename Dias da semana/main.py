def realizar_votacao():
  # Cria um dicionário para armazenar os votos para cada dia da semana
  votos = {
      'segunda': 0,
      'terça': 0,
      'quarta': 0,
      'quinta': 0,
      'sexta': 0
  }

  # Solicita o número de colaboradores que participarão da votação
  while True:
      try:
          num_colaboradores = int(input("Informe o número de colaboradores que participarão da votação: "))
          if num_colaboradores <= 0:
              raise ValueError
          break
      except ValueError:
          print("Por favor, insira um número inteiro positivo.")

  # Realiza a votação com cada colaborador
  for i in range(num_colaboradores):
      while True:
          dia_preferencia = input(f"Colaborador {i+1}, escolha um dia da semana (segunda, terça, quarta, quinta ou sexta): ").strip().lower()
          # Verifica se o input é válido e atualiza o dicionário de votos
          if dia_preferencia in votos:
              votos[dia_preferencia] += 1
              break
          else:
              print("Entrada inválida. Por favor, escolha um dia válido (segunda-feira a sexta-feira).")

  # Determina o dia com mais votos
  dia_mais_votado = max(votos, key=votos.get)
  total_votos = votos[dia_mais_votado]

  # Exibe o resultado
  print(f"O dia mais escolhido foi {dia_mais_votado} com {total_votos} votos.")

# Executa a função de votação
realizar_votacao()