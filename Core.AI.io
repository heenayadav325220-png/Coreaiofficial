<!DOCTYPE html>
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
            --cyan-accent: #00f2ff;
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

        .orb-box { display: flex; justify-content: center; margin: 20px 0; }
        .orb {
            width: 100px; height: 100px;
            background: radial-gradient(circle, var(--cyan-accent), #005f73, transparent);
            border-radius: 50%;
            box-shadow: 0 0 40px rgba(0, 242, 255, 0.3);
            animation: breathe 4s infinite ease-in-out;
        }
        @keyframes breathe { 0%, 100% { transform: scale(1); opacity: 0.7; } 50% { transform: scale(1.05); opacity: 1; } }

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
        
        <div class="orb-box">
            <div class="orb"></div>
        </div>

        <nav class="flex-1 p-4 space-y-2 overflow-y-auto">
            <button onclick="setMode('chat')" class="nav-item active w-full flex items-center gap-3 p-3 rounded-xl bg-blue-600/10 text-blue-400 border border-blue-500/20">
                <i data-lucide="message-square" class="w-5 h-5"></i> <span class="text-sm font-bold uppercase tracking-widest">Chat</span>
            </button>
            <button onclick="setMode('image')" class="nav-item w-full flex items-center gap-3 p-3 rounded-xl hover:bg-white/5 text-zinc-400 hover:text-white transition-all">
                <i data-lucide="image" class="w-5 h-5"></i> <span class="text-sm font-bold uppercase tracking-widest">Image</span>
            </button>
        </nav>
        <div class="p-6 border-t border-white/10 text-center text-xs text-zinc-500">Rohit Yadav • Neural Link</div>
    </aside>

    <header class="p-6 glass-panel border-b border-white/10 flex justify-between items-center z-40">
        <button id="menu-toggle" class="lg:hidden p-2 rounded-lg bg-white/5"> <i data-lucide="menu" class="w-6 h-6"></i> </button>
        <div class="flex items-center gap-3">
            <div class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
            <span id="mode-indicator" class="text-[10px] font-mono text-zinc-500 uppercase tracking-widest">System Operational</span>
        </div>
        <button id="dashboard-toggle" class="p-2 rounded-lg bg-white/5"> <i data-lucide="layout-grid" class="w-5 h-5 text-zinc-400"></i> </button>
    </header>

    <main id="chat-area" class="flex-1 overflow-y-auto p-6 space-y-6 pb-40">
        <div class="flex flex-col items-start max-w-[85%]">
            <div class="text-[10px] text-zinc-500 uppercase tracking-widest mb-2 ml-1">CORE AI • System</div>
            <div class="p-4 rounded-2xl rounded-tl-none glass-panel text-sm leading-relaxed">
                Namaste. I am Core AI, founded by Rohit Yadav. Ready for input.
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
                <div class="flex justify-between items-center mb-4"><span class="text-[10px] font-mono text-blue-400 uppercase tracking-widest">Live Status</span><div class="w-1.5 h-1.5 rounded-full bg-red-500 animate-pulse"></div></div>
                <div class="text-sm text-zinc-300">System running at 98% efficiency.</div>
            </div>
            <div class="glass-panel p-6 rounded-3xl">
                <span class="text-[10px] font-mono text-amber-400 uppercase tracking-widest mb-4 block">Memory</span>
                <ul class="space-y-2 text-[11px] text-zinc-400">
                    <li>✓ Industrial Dark Theme</li>
                    <li>✓ Orb System Active</li>
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

        // Speech Recognition
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

        function addMessage(role, text, isImage = false) {
            const div = document.createElement('div');
            div.className = `flex flex-col ${role === 'user' ? 'items-end ml-auto' : 'items-start'} max-w-[85%]`;
            
            let content = '';
            if (isImage) {
                content = `<img src="${text}" class="rounded-lg max-w-full h-auto" />`;
            } else {
                content = text;
            }

            div.innerHTML = `
                <div class="text-[9px] text-zinc-500 uppercase tracking-widest mb-1 mx-1">${role === 'user' ? 'You' : 'CORE AI'}</div>
                <div class="p-4 rounded-2xl ${role === 'user' ? 'rounded-tr-none bg-blue-600' : 'rounded-tl-none glass-panel'} text-sm leading-relaxed">
                    ${content}
                </div>
            `;
            chatArea.appendChild(div);
            chatArea.scrollTop = chatArea.scrollHeight;
        }

        // --- AI API CALL ---
        async function processAI(input) {
            updateUI(true, "Thinking...");
            try {
                let prompt = input;
                if (currentMode === 'image') {
                    prompt = `Generate a detailed image based on this prompt: ${input}`;
                }

                const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${MODEL_NAME}:generateContent?key=${GEMINI_API_KEY}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ contents: [{ parts: [{ text: prompt }] }] })
                });
                
                const data = await response.json();
                const aiText = data.candidates[0].content.parts[0].text;
                
                if (currentMode === 'image') {
                    // Note: This API requires a different approach for true image generation.
                    // For now, this will return a text description to be visualized or use a dummy image.
                    addMessage('model', "Image Generation Mode: " + aiText);
                    speak("Image generation feature requires API configuration for image generation.");
                } else {
                    addMessage('model', aiText);
                    speak(aiText);
                }
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
            currentMode = mode;
            console.log("Mode set to: " + mode);
            document.getElementById('mode-indicator').innerText = mode.toUpperCase() + " ACTIVE";
        }
    </script>
</body>
</html>
