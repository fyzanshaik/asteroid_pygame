_Asteroid_ _GAME_

Made while learning OOP with Pygame!

### Requirements:

-  Python 3.8+
-  uv (for dependency management)

### Installation

1. **Install uv**

If you don’t have `uv` installed, run:

```bash
pip install uv
```

Or, for the latest version:

```bash
pip install --upgrade uv
```

2. **Clone the Repository**

```bash
git clone https://github.com/yourusername/asteroid-game.git
cd asteroid-game
```

3. **Create a Virtual Environment**

```bash
uv venv .venv
```

4. **Activate the Virtual Environment**

-  **On Linux/macOS:**
   ```bash
   source .venv/bin/activate
   ```
-  **On Windows:**
   ```bash
   .venv\Scripts\activate
   ```

5. **Install Dependencies**

```bash
uv pip install -r requirements.txt
```

Or, if you use a `pyproject.toml`:

```bash
uv pip install -r requirements.txt
# or
uv pip install .
```

6. **Run the Game**

```bash
python main.py
```

---

### Development

-  To add new dependencies:
   ```bash
   uv pip install <package>
   ```
-  To update dependencies:
   ```bash
   uv pip install -U <package>
   ```

### Uninstallation

To remove the virtual environment:

```bash
deactivate
rm -rf .venv
```
