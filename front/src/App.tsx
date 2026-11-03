
function App() {
  return (
    <main className='w-120'>
      <div className="flex mb-10">
        <input className="bg-white w-full p-2 rounded-l-md outline-none" type="text" placeholder='tire sua dúvida aqui' />
        <button className="p-2 bg-gray-400 hover:opacity-50 hover:cursor-pointer font-medium rounded-r-md">Enviar</button>
      </div>

      <div className="bg-white">
        <h1 className="bg-gray-500 p-2 text-white font-medium">Resposta do Agente:</h1>
        <p className="p-2 scrollbar-thin overflow-y-scroll max-h-60">
          (resposta do agente)
        </p>
      </div>

    </main>
  )
}

export default App
