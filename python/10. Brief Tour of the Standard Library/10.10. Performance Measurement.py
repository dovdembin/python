from timeit import Timer

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())  # 0.02018369996221736

print(Timer('a,b = b,a', 'a=1; b=2').timeit())  # 0.02013369998894632