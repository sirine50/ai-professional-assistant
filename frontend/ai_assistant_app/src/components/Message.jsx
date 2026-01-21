function Message({ sender, text }) {
  const isUser = sender === "user"

  return (
    <div
      className={`
        flex ${isUser ? "justify-end" : "justify-start"}
        animate-fade-in
      `}
    >
      <div
        className={`
          max-w-lg px-4 py-2 rounded-lg
          ${isUser
            ? "bg-blue-600 text-white"
            : "bg-gray-700 text-gray-100"}
        `}
      >
        {text}
      </div>
    </div>
  )
}

export default Message
