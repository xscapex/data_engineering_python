def nth_largest_key(d, n):
  # Step 1: Convert dictionary values to a list and sort it
  sorted_values = sorted(d.values(), reverse=True)
  # Step 2: Get nth largest value
  nth_largest_value = sorted_values[n-1]
  # Step 3: Return the key corresponding to nth largest value
  for key, value in d.items():
    if value == nth_largest_value:
      return key