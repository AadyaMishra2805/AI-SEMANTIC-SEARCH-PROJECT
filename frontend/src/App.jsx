import { useState } from "react"

function App() {

  const [result, setResult] = useState("")
  const [query, setQuery] = useState("")
  const [fileName, setFileName] = useState("")

  return (

    <div className="min-h-screen bg-[#f5f7fb] px-6 py-10">

      {/* Heading */}
      <div className="text-center mb-10">

        <h1 className="text-4xl font-bold text-gray-800">
          AI Semantic Search
        </h1>

        <p className="text-gray-500 mt-3 text-sm">
          Upload PDFs and perform semantic document retrieval using AI.
        </p>

      </div>

      {/* Main Layout */}
      <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-8">

        {/* LEFT PANEL */}
        <div className="bg-white rounded-3xl shadow-[0_10px_40px_rgba(0,0,0,0.08)] p-6 border border-gray-200">

          {/* Feature Tags */}
          <div className="flex gap-3 flex-wrap mb-5">

            <div className="bg-green-100 text-green-700 px-4 py-2 rounded-xl text-xs font-medium">
              ChromaDB
            </div>

            <div className="bg-blue-100 text-blue-700 px-4 py-2 rounded-xl text-xs font-medium">
              Semantic Search
            </div>

            <div className="bg-purple-100 text-purple-700 px-4 py-2 rounded-xl text-xs font-medium">
              MiniLM Embeddings
            </div>

          </div>

          {/* Upload Box */}
          <div className="border-2 border-dashed border-gray-300 rounded-2xl p-10 bg-gray-50 text-center">

            <p className="text-gray-600 text-sm">
              Upload your PDF document
            </p>

            <label className="inline-block mt-4 cursor-pointer bg-[#16a34a] hover:bg-[#15803d] text-white px-5 py-2 rounded-xl text-sm">

              Choose PDF

              <input
                type="file"
                accept=".pdf"
                hidden
                onChange={(e) => {

                  if (e.target.files[0]) {
                    setFileName(e.target.files[0].name)
                  }

                }}
              />

            </label>

            {fileName && (

              <p className="mt-4 text-sm text-gray-700">
                Selected: {fileName}
              </p>

            )}

          </div>

          {/* Query Input */}
          <div className="mt-6">

            <textarea
              placeholder="Ask questions about the uploaded document..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              className="w-full border border-gray-300 rounded-2xl p-4 h-52 resize-none outline-none text-sm focus:ring-2 focus:ring-green-500"
            />

          </div>

          {/* Search Button */}
          <div className="flex justify-end mt-5">

            <button

              onClick={async () => {

                try {

                  const response = await fetch(
                    `http://127.0.0.1:8000/search?query=${query}`
                  )

                  const data = await response.json()

                  setResult(data.results)

                }

                catch (error) {

                  setResult("Backend connection failed")

                }

              }}

              className="bg-[#16a34a] hover:bg-[#15803d] text-white px-7 py-3 rounded-2xl text-sm font-medium"
            >
              Search
            </button>

          </div>

        </div>

        {/* RIGHT PANEL */}
        <div className="space-y-5">

          {Array.isArray(result) ? (

            result.map((item, index) => (

              <div
                key={index}
                className="bg-white rounded-3xl shadow-[0_10px_40px_rgba(0,0,0,0.08)] border border-gray-200 p-6"
              >

                <h2 className="text-lg font-semibold text-gray-800 mb-4">
                  Result {index + 1}
                </h2>

                <div className="text-sm text-gray-700 leading-7">
                  {item}
                </div>

              </div>

            ))

          ) : result ? (

            <div className="bg-white rounded-3xl shadow-[0_10px_40px_rgba(0,0,0,0.08)] border border-gray-200 p-6">

              <div className="text-sm text-gray-700">
                {result}
              </div>

            </div>

          ) : (

            <div className="bg-white rounded-3xl shadow-[0_10px_40px_rgba(0,0,0,0.08)] border border-gray-200 p-6 h-[650px] flex items-center justify-center">

              <div className="text-center">

                <p className="text-gray-400 text-sm">
                  Your semantic search results will appear here.
                </p>

              </div>

            </div>

          )}

        </div>

      </div>

    </div>

  )
}

export default App