## Objective
Delete the "2nd" resource (index 1) from a set of 5 Terraform-managed resources defined using `count`, without affecting the other resources.

## Recommended Solution: Migrate to `for_each`

1. **Snapshot the current state into local names**

   Use Terraform state commands to move the existing resources to named keys.

   Example (adjust for your actual resource type and name):

   ```bash
   terraform state list
