from functools import wraps

def ensure_first_arg_is(val):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			if args and args[0] != val:
				return f"First arg needs to be {val}"
			return fn(*args, **kwargs)
		return wrapper
	return inner


@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)

# print(fav_foods("burrito", "ice cream")) # ('burrito', 'ice cream')
# print(fav_foods("ice cream", "burrito")) # 'Invalid! First argument must be burrito'

@ensure_first_arg_is(10)
def sum_num(*args):
    print(sum(args))

sum_num(10,20)
print(sum_num(20,10))
sum_num(10,20,30,40,50,60,70,80)

