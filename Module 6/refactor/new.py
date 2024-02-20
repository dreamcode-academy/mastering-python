import timeit
test_statement = "loop_sum(range(1000))"
setup_statement = "from timeit_md import loop_sum"

execution_time = timeit.timeit(stmt=test_statement,setup=setup_statement, number=10000)
print(f"Execution time of loop sum: {execution_time}")