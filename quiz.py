print('Welcome to my computer quiz!')

playing = input('Do you want to play?')

print(playing)

if playing != 'yes':
  quit()
  
print('Okay! Lets Play :)')
score = 0

answer = input('What does CPU Stand for?')

if answer.lower() == 'central processing unit':
  print('correct!')
  score+=1
else:
  print('Incorrect'  )
  
answer = input('What does GPU Stand for?')

if answer.lower() == 'graphics processing unit':
  print('correct!')
  score+=1
else:
  print('Incorrect'  )
  
answer = input('What does RAM Stand for?')

if answer.lower() == 'random access memory':
  print('correct!')
  score+=1
else:
  print('Incorrect'  )
  
answer = input('What does PSU Stand for?')

if answer.lower() == 'power supply':
  print('correct!')
  score+=1
else:
  print('Incorrect'  )
  

print('You got '+ str(score)+' questions correct!')
print('You got '+ str((score/4)*100)+' %.')


  