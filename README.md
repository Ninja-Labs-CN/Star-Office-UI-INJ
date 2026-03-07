# Star Office UI

This repository contains the Star Office UI project, a pixel-art styled office dashboard for visualizing AI agent work status in real-time.

## Recent Updates

- Work Log panel (formerly "Yesterday Notes") now displays real-time task updates
- Office name updated to **Vincent Co.Tech** across all language versions
- Automatic state synchronization via `set_state.py`
- Scrollable log area with larger font for better readability

## Features

- Real-time work status visualization
- Automatic state management with 6 states: `idle`, `writing`, `researching`, `executing`, `syncing`, `error`
- Multi-language support (Chinese, English, Japanese)
- Responsive design for desktop and mobile
- Integration with OpenClaw agent framework
- Live log updates with work record panel

## Quick Start

### Installation

```bash
git clone https://github.com/ChuhanJin/Star-Office-UI-INJ.git
cd Star-Office-UI-INJ

python3 -m pip install -r backend/requirements.txt
cp state.sample.json state.json
```

### Running the Server

```bash
cd backend
python3 app.py
```

Open your browser at `http://127.0.0.1:19000` to access the UI.

### Updating the Work Log

```bash
python3 set_state.py executing "Your task description here"
python3 set_state.py idle "Task complete"
```

The Work Log panel will automatically refresh with the latest status message.

## Project Structure

```
Star-Office-UI-INJ/
├── backend/              # Flask backend server
├── frontend/             # HTML/CSS/JS UI files
│   ├── index.html        # Main UI page
│   ├── log.txt           # Real-time work log
│   └── layout.js         # UI logic
├── set_state.py          # State management script
├── state.sample.json     # State template
├── README.md             # This file
└── LICENSE               # MIT License
```

## API Endpoints

- `GET /health` - Health check
- `GET /status` - Get current status
- `POST /set_state` - Update state
- `GET /yesterday-memo` - Get work log

## Configuration

Edit `state.json` to customize office appearance, agent names, and settings.

## License

MIT © OpenClaw contributors

## Support

For issues, feature requests, or contributions, please open an issue or pull request on GitHub.
