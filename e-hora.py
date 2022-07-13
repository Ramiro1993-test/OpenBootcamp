from datetime import datetime

def hora():
  hactual = datetime.now().time()
  hora=datetime.strptime('07:00:00',"%X").time()
  
  if hactual > hora:
     return f'Es hora de de ir a casa, son las {hactual}'
  elif hactual < hora:
     hfalta = hactual - hora
     return f'Faltan {hfalta} para terminar la jornada'
