import { useState } from 'react'
import './App.css'

function App() {
  const [note, setNote] = useState('')

  const saveNote = async (noteData) => {
    const response = await fetch('http://127.0.0.1:5000/save_note', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({noteData})
    }); 

    if (!response.ok) {
      throw new Error(`Error Saving Note ${response.status}`)
    }

    const data = await response.json();
    console.log('Success:', data);
  }

  return (
    <div>
      <textarea type='text' 
      id='note' 
      name='note' 
      value={note}
      onChange={(event) => {setNote(event.target.value);}}
      />
      <button onClick={() => saveNote(note)}>Save</button>
    </div>
  )
}

export default App
