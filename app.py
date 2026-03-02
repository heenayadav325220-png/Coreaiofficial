# --- 1. DARK INDUSTRIAL THEME CSS ---
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,1,0" rel="stylesheet" />
    
    <style>
    /* Full Dark Mode with Boltshift Gradient */
    .stApp {
        background: radial-gradient(circle at top right, #07191e 0%, #000000 100%);
        color: #acb2b1;
    }

    /* Standard Grid Boxes (Inspired by Boltshift) */
    .feature-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        transition: 0.4s ease;
    }
    .feature-card:hover {
        border-color: #00f2ff;
        background: rgba(0, 242, 255, 0.05);
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.1);
    }

    /* Standard Classic Icons (No Emoji) */
    .material-symbols-rounded {
        font-size: 32px !important;
        color: #00f2ff;
    }

    /* Jarvas Style Orb */
    .orb-box { display: flex; justify-content: center; margin: 30px 0; }
    .orb {
        width: 130px; height: 130px;
        background: radial-gradient(circle, #00f2ff, #005f73, transparent);
        border-radius: 50%;
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.3);
        animation: breathe 6s infinite ease-in-out;
    }
    @keyframes breathe { 0%, 100% { transform: scale(1); opacity: 0.7; } 50% { transform: scale(1.05); opacity: 1; } }

    /* Custom Input Bar (Like the one with Mic in your photo) */
    .stChatInputContainer {
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
        background: rgba(10, 10, 10, 0.6) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE UI LAYOUT ---

# Top Orb (Jarvas Vibe)
st.markdown('<div class="orb-box"><div class="orb"></div></div>', unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; letter-spacing: 5px; font-weight: 200;'>CORE AI</h2>", unsafe_allow_html=True)

# The 4 Feature Boxes (Standard Icons)
st.write("##")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="feature-card"><span class="material-symbols-rounded">psychology</span><p style="font-size:11px; margin-top:10px; color:#666;">NEURAL LINK</p></div>', unsafe_allow_html=True)
    if st.button("ACTIVATE OPUS", use_container_width=True): pass

    st.markdown('<div class="feature-card"><span class="material-symbols-rounded">visibility</span><p style="font-size:11px; margin-top:10px; color:#666;">VISUAL CORE</p></div>', unsafe_allow_html=True)
    if st.button("ACTIVATE VISION", use_container_width=True): pass

with col2:
    st.markdown('<div class="feature-card"><span class="material-symbols-rounded">videocam</span><p style="font-size:11px; margin-top:10px; color:#666;">CINEMA GEN</p></div>', unsafe_allow_html=True)
    if st.button("ACTIVATE VIDEO", use_container_width=True): pass

    st.markdown('<div class="feature-card"><span class="material-symbols-rounded">mic</span><p style="font-size:11px; margin-top:10px; color:#666;">VOICE LINK</p></div>', unsafe_allow_html=True)
    if st.button("ACTIVATE NICK", use_container_width=True): pass

# Input Section (The "Standard" way)
st.write("---")
DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CORE AI | Neural Interface</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=JetBrains+Mono&display=swap');
        
        :root {
            --bg: #050505;
            --accent: #3b82f6;
            --glass: rgba(255, 255, 255, 0.03);
            --border: rgba(255, 255, 255, 0.1);
        }

        body {
            background-color: var(--bg);
            color: #fff;
            font-family: 'Inter', sans-serif;
            overflow: hidden;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }

        .neural-grid {
            background-image: radial-gradient(var(--border) 1px, transparent 1px);
            background-size: 30px 30px;
        }

        .glass-panel {
            background: var(--glass);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border);
        }

        .sidebar-transition { transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1); }

        .mic-active {
            box-shadow: 0 0 30px rgba(59, 130, 246, 0.5);
            transform: scale(1.05);
            border-color: rgba(59, 130, 246, 0.5) !important;
        }

        .dashboard-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.9);
            backdrop-filter: blur(20px);
            z-index: 100;
            transform: translateY(100%);
            transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .dashboard-overlay.open { transform: translateY(0); }

        @keyframes pulse-ring { 0% { transform: scale(0.8); opacity: 0.5; } 100% { transform: scale(1.5); opacity: 0; } }
        .pulse-ring { position: absolute; width: 100%; height: 100%; border: 2px solid var(--accent); border-radius: 50%; animation: pulse-ring 2s infinite; }

        /* Custom Scrollbar */
        #chat-area::-webkit-scrollbar { width: 4px; }
        #chat-area::-webkit-scrollbar-thumb { background: var(--border); border-radius: 10px; }
    </style>
</head>
<body class="neural-grid">

    <aside id="sidebar" class="fixed lg:relative inset-y-0 left-0 w-72 glass-panel border-r border-white/10 z-50 sidebar-transition -translate-x-full lg:translate-x-0 flex flex-col">
        <div class="p-6 border-b border-white/10 flex items-center gap-3">
            <div class="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center shadow-[0_0_15px_rgba(37,99,235,0.4)]">
                <i data-lucide="zap" class="w-5 h-5 text-white"></i>
            </div>
            <h1 class="text-xl font-black tracking-tighter uppercase">CORE <span class="text-blue-500">AI</span></h1>
        </div>
        <nav class="flex-1 p-4 space-y-2 overflow-y-auto">
            <button onclick="setMode('chat')" class="nav-item active w-full flex items-center gap-3 p-3 rounded-xl bg-blue-600/10 text-blue-400 border border-blue-500/20">
                <i data-lucide="message-square" class="w-5 h-5"></i> <span class="text-sm font-bold uppercase tracking-widest">Chat</span>
            </button>
            <button onclick="setMode('image')" class="nav-item w-full flex items-center gap-3 p-3 rounded-xl hover:bg-white/5 text-zinc-400 hover:text-white transition-all">
                <i data-lucide="image" class="w-5 h-5"></i> <span class="text-sm font-bold uppercase tracking-widest">Image Gen</span>
            </button>
            <button onclick="setMode('video')" class="nav-item w-full flex items-center gap-3 p-3 rounded-xl hover:bg-white/5 text-zinc-400 hover:text-white transition-all">
                <i data-lucide="video" class="w-5 h-5"></i> <span class="text-sm font-bold uppercase tracking-widest">Video Gen</span>
            </button>
            <button onclick="setMode('voice')" class="nav-item w-full flex items-center gap-3 p-3 rounded-xl hover:bg-white/5 text-zinc-400 hover:text-white transition-all">
                <i data-lucide="mic-2" class="w-5 h-5"></i> <span class="text-sm font-bold uppercase tracking-widest">Voice</span>
            </button>
            <button onclick="setMode('mood')" class="nav-item w-full flex items-center gap-3 p-3 rounded-xl hover:bg-white/5 text-zinc-400 hover:text-white transition-all">
                <i data-lucide="heart" class="w-5 h-5"></i> <span class="text-sm font-bold uppercase tracking-widest">Mood</span>
            </button>
        </nav>
        <div class="p-6 border-t border-white/10 text-center text-xs text-zinc-500">Rohit Yadav • Neural Link</div>
    </aside>

    <header class="p-6 glass-panel border-b border-white/10 flex justify-between items-center z-40">
        <button id="menu-toggle" class="lg:hidden p-2 rounded-lg bg-white/5"> <i data-lucide="menu" class="w-6 h-6"></i> </button>
        <div class="flex items-center gap-3">
            <div class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
            <span id="mode-indicator" class="text-[10px] font-mono text-zinc-500 uppercase tracking-widest">Neural Chat Active</span>
        </div>
        <button id="dashboard-toggle" class="p-2 rounded-lg bg-white/5"> <i data-lucide="layout-grid" class="w-5 h-5 text-zinc-400"></i> </button>
    </header>

    <main id="chat-area" class="flex-1 overflow-y-auto p-6 space-y-6 pb-40">
        <div class="flex flex-col items-start max-w-[85%]">
            <div class="text-[10px] text-zinc-500 uppercase tracking-widest mb-2 ml-1">CORE AI • System</div>
            <div class="p-4 rounded-2xl rounded-tl-none glass-panel text-sm leading-relaxed">
                Namaste. I am Core AI, founded by Rohit Yadav. How can I assist you?
            </div>
        </div>
    </main>

    <footer class="fixed bottom-0 left-0 right-0 p-8 glass-panel border-t border-white/10 flex flex-col items-center gap-6 z-30">
        <div id="status-text" class="text-[11px] font-mono text-zinc-500 uppercase tracking-[0.3em] animate-pulse">Ready for Input</div>
        <button id="mic-btn" class="w-20 h-20 rounded-full bg-white/5 border border-white/10 flex items-center justify-center transition-all duration-300 hover:bg-white/10 active:scale-95 group">
            <div id="mic-icon-container" class="relative">
                <div id="pulse" class="hidden pulse-ring"></div>
                <i data-lucide="mic" id="mic-icon" class="w-8 h-8 text-zinc-400 group-hover:text-white transition-colors"></i>
                <i data-lucide="square" id="stop-icon" class="w-8 h-8 text-blue-400 hidden"></i>
            </div>
        </button>
    </footer>

    <div id="dashboard" class="dashboard-overlay p-6 overflow-y-auto z-50">
        <div class="flex justify-between items-center mb-8">
            <h2 class="text-2xl font-black uppercase tracking-tighter">Neural <span class="text-blue-500">Dashboard</span></h2>
            <button id="close-dashboard" class="p-2 rounded-full bg-white/10"><i data-lucide="x" class="w-6 h-6"></i></button>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="glass-panel p-6 rounded-3xl border-blue-500/20">
                <div class="flex justify-between items-center mb-4"><span class="text-[10px] font-mono text-blue-400 uppercase tracking-widest">Live Cricket</span><div class="w-1.5 h-1.5 rounded-full bg-red-500 animate-pulse"></div></div>
                <div class="flex justify-between items-center"><div class="text-center"><div class="text-2xl font-black">IND 245/4</div></div><div class="text-zinc-500 font-mono text-xs">vs</div><div class="text-center"><div class="text-2xl font-black text-zinc-500">AUS</div></div></div>
            </div>
            <div class="glass-panel p-6 rounded-3xl">
                <span class="text-[10px] font-mono text-amber-400 uppercase tracking-widest mb-4 block">Neural Memory</span>
                <ul class="space-y-2 text-[11px] text-zinc-400">
                    <li>✓ Dark mode active</li>
                    <li>✓ Project: CORE AI</li>
                </ul>
            </div>
        </div>
    </div>

    <script>
        lucide.createIcons();

        // --- CONFIGURATION ---
        const GEMINI_API_KEY = "AIzaSyAu_a17XYn3WStXjmfEeTH-hcUW_CDYDkg";
        const MODEL_NAME = "gemini-1.5-flash";
        // ---------------------

        let isActive = false;
        let currentMode = 'chat';
        const chatArea = document.getElementById('chat-area');
        const micBtn = document.getElementById('mic-btn');
        const micIcon = document.getElementById('mic-icon');
        const stopIcon = document.getElementById('stop-icon');
        const pulse = document.getElementById('pulse');
        const statusText = document.getElementById('status-text');
        const dashboard = document.getElementById('dashboard');

        // Sidebar Toggles
        const menuToggle = document.getElementById('menu-toggle');
        const sidebar = document.getElementById('sidebar');
        menuToggle.onclick = () => sidebar.classList.toggle('-translate-x-full');

        // Dashboard Toggles
        document.getElementById('dashboard-toggle').onclick = () => dashboard.classList.add('open');
        document.getElementById('close-dashboard').onclick = () => dashboard.classList.remove('open');

        // Speech Recognition Setup
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = SpeechRecognition ? new SpeechRecognition() : null;

        if (recognition) {
            recognition.continuous = false;
            recognition.onresult = (e) => {
                const text = e.results[0][0].transcript;
                addMessage('user', text);
                processAI(text);
            };
        }

        micBtn.addEventListener('click', () => {
            if (isActive) stopAll();
            else startInteraction();
        });

        function startInteraction() {
            isActive = true;
            window.speechSynthesis.cancel();
            updateUI(true, "Listening...");
            if (recognition) recognition.start();
        }

        function stopAll() {
            isActive = false;
            window.speechSynthesis.cancel();
            if (recognition) recognition.stop();
            updateUI(false, "Ready for Input");
        }

        function updateUI(active, text) {
            statusText.innerText = text;
            if (active) {
                micBtn.classList.add('mic-active');
                pulse.classList.remove('hidden');
                micIcon.classList.add('hidden');
                stopIcon.classList.remove('hidden');
            } else {
                micBtn.classList.remove('mic-active');
                pulse.classList.add('hidden');
                micIcon.classList.remove('hidden');
                stopIcon.classList.add('hidden');
            }
        }

        function addMessage(role, text) {
            const div = document.createElement('div');
            div.className = `flex flex-col ${role === 'user' ? 'items-end ml-auto' : 'items-start'} max-w-[85%] animate-in fade-in slide-in-from-bottom-2`;
            div.innerHTML = `
                <div class="text-[9px] text-zinc-500 uppercase tracking-widest mb-1 mx-1">${role === 'user' ? 'You' : 'CORE AI'}</div>
                <div class="p-4 rounded-2xl ${role === 'user' ? 'rounded-tr-none bg-blue-600' : 'rounded-tl-none glass-panel'} text-sm leading-relaxed">
                    ${text}
                </div>
            `;
            chatArea.appendChild(div);
            chatArea.scrollTop = chatArea.scrollHeight;
        }

        // --- AI API CALL ---
        async function processAI(input) {
            updateUI(true, "Thinking...");
            try {
                const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${MODEL_NAME}:generateContent?key=${GEMINI_API_KEY}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ contents: [{ parts: [{ text: input }] }] })
                });
                const data = await response.json();
                const aiText = data.candidates[0].content.parts[0].text;
                addMessage('model', aiText);
                speak(aiText);
            } catch (error) {
                addMessage('model', "Neural Error: " + error.message);
                stopAll();
            }
        }

        function speak(text) {
            updateUI(true, "Speaking...");
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.onend = () => stopAll();
            window.speechSynthesis.speak(utterance);
        }

        function setMode(mode) {
            // Functionality to be added
            console.log("Mode set to: " + mode);
        }
    </script>
</body>
</html>
