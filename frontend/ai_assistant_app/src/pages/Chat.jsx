import Header from "../components/Header"
import ChatBox from "../components/ChatBox"

function Chat() {
  return (
    <div className="flex flex-col h-screen">
      <Header />
      <ChatBox />
    </div>
  )
}

export default Chat