css = """
<style>
body {
    background-color: #f9fafb;
    font-family: 'Segoe UI', sans-serif;
}

.chat-container {
    padding: 1rem;
    border-radius: 12px;
    margin-bottom: 1rem;
    max-width: 95%;
    word-wrap: break-word;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.user-message {
    background-color: #e0f7fa;
    color: #006064;
    margin-left: auto;
    text-align: right;
}

.bot-message {
    background-color: #f1f8e9;
    color: #33691e;
    margin-right: auto;
    text-align: left;
}

.chat-box {
    display: flex;
    flex-direction: column;
    gap: 10px;
    max-height: 65vh;
    overflow-y: auto;
    padding-right: 10px;
    margin-bottom: 1rem;
}
</style>
"""

user_template = """
<div class="chat-container user-message">
    {{MSG}}
</div>
"""

bot_template = """
<div class="chat-container bot-message">
    {{MSG}}
</div>
"""
