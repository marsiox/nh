import pytest
from nordhealth import PairFinder

def test_find_unique_pair_sums():
  nums = [1, 2, 3, 4, 5]
  pf = PairFinder(nums)
  assert pf.find_unique_pair_sums(nums) == {3, 4, 5, 6, 7, 8, 9}

def test_find_pairs_for_sum():
  nums = [1, 2, 3, 4, 5]
  pf = PairFinder(nums)
  assert pf.find_pairs_for_sum(nums, 3) == [(1, 2)]
  assert pf.find_pairs_for_sum(nums, 4) == [(1, 3)]
  assert pf.find_pairs_for_sum(nums, 5) == [(2, 3), (1, 4)]
  assert pf.find_pairs_for_sum(nums, 6) == [(2, 4), (1, 5)]
  assert pf.find_pairs_for_sum(nums, 7) == [(3, 4), (2, 5)]
  assert pf.find_pairs_for_sum(nums, 8) == [(3, 5)]
  assert pf.find_pairs_for_sum(nums, 9) == [(4, 5)]
