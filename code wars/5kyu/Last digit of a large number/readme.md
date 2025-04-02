see https://www.codewars.com/kata/5511b2f550906349a70004e1/train/go

You may assume that the input will always be valid.

Examples
lastDigit 4 1             `shouldBe` 4
lastDigit 4 2             `shouldBe` 6
lastDigit 9 7             `shouldBe` 9
lastDigit 10 (10^10)      `shouldBe` 0
lastDigit (2^200) (2^300) `shouldBe` 6

For solution some explication here :
https://brilliant.org/wiki/finding-the-last-digit-of-a-power/ or https://www.geeksforgeeks.org/find-last-digit-of-ab-for-large-numbers/