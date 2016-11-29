residence_limit = 90  # 45, 60
schengen_constraint = 180
visits = []
date_in_future = int()


#берём визиты с visits.txt
with open ('visits.txt') as file:
	for line in file:
		visits.append([int(x) for x in line.split()])

print (visits)
def date_difference (leave, arrive):
	result = leave - arrive + 1
	return result


def visit_length (visit):
	return date_difference(visit[1], visit[0])


def print_mistake(visits):
  for visit in visits:
	  for visit1 in visits:
		  if visit[1] < visit[0]:
		    raise Exception('Ошибка, дата отъезда раньше даты приезда', visit)
		  if visit != visit1:
			  if visit[0] <= visit1[0] <= visit[1]:
				  raise Exception('Ошибка, нарушение условий пребывания', visit)
			  if visit[0] <= visit1[1] <= visit[1]:
				  raise Exception('Ошибка, нарушение условий пребывания', visit)


def get_days_for_visits(visits):
	days_for_visits = []
	for visit in visits:
	    days_for_visit = 0
	    for past_visit in visits:
	        if visit[0] - schengen_constraint < past_visit[0] < visit[0]:
	            days_for_visit += visit_length(past_visit)
	    days_for_visit += visit_length(visit)
	    days_for_visits.append(days_for_visit)
	return days_for_visits
	

def print_days_future_visit(visits, date_in_future):
	visits_for_future = visits + [[date_in_future, date_in_future]]
	days_for_future_visits = get_days_for_visits(visits_for_future)
	days_in_es = residence_limit - days_for_future_visits[len(days_for_future_visits) - 1] + 1
	print ('Если въедем %s числа, сможем провести в шенгене %s дней' % (date_in_future, days_in_es))


def print_residence_limit_violation(visits):
	days_for_visits = get_days_for_visits(visits)
	

	for visit, total_days in zip(visits, days_for_visits):
	    if total_days > residence_limit:
	        overstay_time = total_days - residence_limit
	        print('Во время визита', visit, 'количество время пребывания превышено на', overstay_time, 'дней')


def print_start_end(visits):
  print ('Начало')
  start = int(input())
  print('Конец')
  end = int(input())
  visits.append([start, end])
  if user_input == 'q':
    print_mistake(visits)
    print('Ваши предполагаемые поездки:',visits)
    visits.remove([start, end])


def print_visits_v(visits):
  if user_input == 'v':
    print_start_end(visits)


def print_visits_q(visits):
    if user_input == 'q':
      print_start_end(visits)

 
def print_visits_p(visits):
  if user_input == 'p':
    print('введите дату')
    date = int(input())
    date_in_future = date
    print_days_future_visit(visits, date_in_future)


while True:
	print('v - добавить визит')
	print('p - добавить дату визита для проверки остаточных дней')
	print('q - введите возможный визит')
	print('e - выход')
	user_input = input()
	print_visits_v(visits)
	print_visits_p(visits)
	print_visits_q(visits)
	print_mistake(visits)
	print_residence_limit_violation(visits)
	if user_input == 'e':
	  break


#вписываем всем визиты в new_visits.txt
with open ('new_visits.txt', 'w') as new_visits:
	new_visits.write(str(visits))


print('Ваши запланированные поездки:',visits)
