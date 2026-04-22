## What changed
Added a limit on failed sign-in attempts. Users can now try up to 3 times before further attempts are blocked.

## Why
Some users were repeatedly attempting to log in with incorrect passwords. This change prevents unlimited attempts and reduces the risk of brute-force attacks.

## How to test
1. Go to the sign-in page
2. Enter an incorrect password three times
3. Attempt a fourth login
4. Verify that further attempts are blocked or an error message is shown

## Checklist
- [ ] Tests added or updated
- [ ] README updated if behavior changed
- [ ] No debug code left