### I. Troubleshooting: RuntimeError: Parent directory ../models does not exist.
- **Issue**: PyTorch failed to save the model because the models/ folder was missing in the local environment.
- **Reason**: Git does not track empty folders. Even though I created it on GitHub, it wasn't downloaded to my laptop.
- **Solution**: Manually created the folder using mkdir models.

### II. Troubleshooting: Relative Path Confusion
- **Issue**: RuntimeError: Parent directory ../models does not exist.
- **What I learned**: Using ../ in code can be risky because it depends on where you run the script from.
  -	If I run the script from the root, ../ points to the folder outside the project.
  -	Best Practice: Use os.makedirs() to ensure the directory exists before saving, and avoid hardcoding relative paths like ../ when possible. This is like setting a proper "minimap" in Valorant so you don't get lost!

