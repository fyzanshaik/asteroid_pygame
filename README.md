_Asteroid_ _GAME_

Made while learning OOP with Pygame!

Current features to add:

-  [x] Add a scoring system
-  [x] Implement multiple lives and respawning
-  [] Add an explosion effect for the asteroids
-  [] Add acceleration to the player movement
-  [] Make the objects wrap around the screen instead of disappearing
-  [] Add a background image
-  [] Create different weapon types
-  [] Make the asteroids lumpy instead of perfectly round
-  [] Make the ship have a triangular hit box instead of a circular one
-  [] Add a shield power-up
-  [] Add a speed power-up
-  [] Add bombs that can be dropped

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
