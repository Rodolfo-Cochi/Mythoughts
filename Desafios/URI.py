#GameTime 
''' hora_inicio = int(input())
hora_final = int(input())

if hora_inicio < hora_final:
    horas_jogadas = hora_final - hora_inicio
elif hora_inicio > hora_final:
    horas_jogadas = hora_inicio - hora_final
    horas_jogadas = 24 - horas_jogadas
else:
    horas_jogadas = 24

print("O JOGO DUROU %i HORA(S)" %horas_jogadas) '''

#GameTime 2
hora_inicio = int(input())
minuto_inicio = int(input())
hora_final = int(input())
minuto_final = int(input())

horas_jogadas = hora_final - hora_inicio

minutos_jogados = minuto_final - minuto_inicio

if (horas_jogadas > 0) and (minutos_jogados > 0):
    minutos_jogados = minutos_jogados + (horas_jogadas*60)
    horas_jogadas = minutos_jogados//60
    minutos_jogados = minutos_jogados%60

elif(horas_jogadas < 0 ) and (minutos_jogados > 0):
    horas_jogadas = 24 + horas_jogadas
    minutos_jogados = minutos_jogados + (horas_jogadas*60)
    horas_jogadas = minutos_jogados//60
    minutos_jogados = minutos_jogados%60 

elif(horas_jogadas > 0) and (minutos_jogados < 0):
    minutos_jogados = minutos_jogados + (horas_jogadas*60)
    horas_jogadas = minutos_jogados//60
    minutos_jogados = minutos_jogados%60

elif(horas_jogadas < 0) and (minutos_jogados < 0):
    horas_jogadas = 24 + horas_jogadas
    minutos_jogados = minutos_jogados + (horas_jogadas*60)
    horas_jogadas = minutos_jogados//60
    minutos_jogados = minutos_jogados%60 

elif(horas_jogadas == 0) and (minutos_jogados > 0):
    minutos_jogados = minutos_jogados

else:
    horas_jogadas = 24 + horas_jogadas
    minutos_jogados = minutos_jogados + (horas_jogadas*60)
    horas_jogadas = minutos_jogados//60
    minutos_jogados = minutos_jogados%60 
    
print(f'O JOGO DUROU {horas_jogadas} HORA(S) E {minutos_jogados} MINUTO(S)')