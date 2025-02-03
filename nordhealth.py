class PairFinder:
  MIN_PAIRS = 2

  def __init__(self, collection):
    self.collection = collection

  """
  Finds the sums of all unique pairs in a collection.
  Given the array [1, 2, 3, 4, 5], the unique pairs are:
  1-2 1-3 1-4 1-5
  2-3 2-4 2-5
  3-4 3-5
  4-5
  """
  def find_unique_pair_sums(self, collection):
    sums = set()

    for i in range(len(collection)):
      for j in range(i + 1, len(collection)):  # Start j from i+1 to avoid duplication
        sums.add(collection[i] + collection[j])

    return sums


  def find_pairs_for_sum(self, collection, target_sum):
    pairs = []
    recorded_elements = {}  # Hash table to store numbers and their indices

    for i, num in enumerate(collection):
        complement = target_sum - num
        if complement in recorded_elements:
            pairs.append((complement, num))
        recorded_elements[num] = i  # Store the number and its index

    return pairs


  def print_pairs(self, pairs, sum):
    pair_strings = " ".join(str(pair) for pair in pairs)
    print(f"Pairs: {pair_strings} have sum: {sum}")


nums = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]

pf = PairFinder(nums)
for sum in pf.find_unique_pair_sums(nums):
  pairs = pf.find_pairs_for_sum(nums, sum)

  if len(pairs) >= PairFinder.MIN_PAIRS:
    pf.print_pairs(pairs, sum)