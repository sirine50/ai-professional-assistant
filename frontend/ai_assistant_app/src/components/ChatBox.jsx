import Message from "./Message"

function ChatBox() {
  const isLoading = true // fake for now

  return (
    <div className="flex flex-col flex-1">

      {/* Messages area */}
      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        <Message sender="ai" text="Hello 👋 How can I help you today?" />
        <Message sender="user" text="I want to build a cool app." />
        <Message sender="ai" text="Nice. Let’s do something impressive." />

        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-gray-700 px-4 py-2 rounded-lg text-sm italic animate-pulse">
              AI is typing...
            </div>
          </div>
        )}
      </div>

      {/* Input area */}
      <div className="p-4 border-t border-gray-700 bg-gray-800">
        <div className="flex gap-3">
          <input
            type="text"
            placeholder="Type your message..."
            className="flex-1 bg-gray-700 text-white rounded-lg px-4 py-2 focus:outline-none"
          />
          <button
            className="
              bg-blue-600 px-5 py-2 rounded-lg font-semibold
              hover:bg-blue-500
              active:scale-95
              transition-all duration-150
            "
          >
            Send
          </button>
        </div>
      </div>

    </div>
  )
}

export default ChatBox
