"use client";

import { useState } from "react";

export default function InboxPage() {
  const [messages, setMessages] = useState([
    { sender: "customer", content: "Hi, I placed my order yesterday but haven't received any update." },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const generateReply = async () => {
    setLoading(true);
    // Call backend API
    const response = await fetch(`/api/backend/conversations/1/generate-reply`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: messages[0].content, personality: "Professional" }),
    });
    const data = await response.json();
    setMessages([...messages, { sender: "ai", content: data.generated_response }]);
    setLoading(false);
  };

  return (
    <div className="flex h-screen p-4 gap-4">
      <div className="w-1/3 bg-card rounded-lg p-4 border border-border">
          <h2 className="font-bold mb-4">Conversations</h2>
          {/* List items */}
      </div>
      <div className="w-2/3 bg-card rounded-lg p-4 flex flex-col border border-border">
        <div className="flex-1 overflow-y-auto mb-4 space-y-4">
          {messages.map((m, i) => (
            <div key={i} className={`p-3 rounded-lg ${m.sender === "ai" ? "bg-primary/10 ml-10" : "bg-secondary mr-10"}`}>
              <p className="text-xs text-foreground/50 uppercase">{m.sender}</p>
              <p>{m.content}</p>
            </div>
          ))}
          {loading && <p className="text-sm text-primary animate-pulse">AI is thinking...</p>}
        </div>
        <div className="flex gap-2">
            <input className="flex-1 bg-input p-2 rounded-lg" value={input} onChange={(e) => setInput(e.target.value)} />
            <button className="bg-primary text-primary-foreground px-4 py-2 rounded-lg" onClick={generateReply}>Generate AI Reply</button>
        </div>
      </div>
    </div>
  );
}
