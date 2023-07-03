def removeDuplicate(n, s):
  # Base case
  if n < 2:
    return s

  if n == 2 and n[0] == n[1]:
    return s
  #Induction hypothesis
  small_otp = ""
  # Induction step
  if s[0] == s[1]:
    # add only one chr out of these two
    # ask recursion to handle the rest
    small_otp = removeDuplicate(n-2, s[2:])
  else:
    # if first two chr are not duplication
    # ask recursion to handle the rest
    small_otp = removeDuplicate(n-1, s[1:])
  if s[0] == small_otp[0]:
    return small_otp
  return s[0] + small_otp
