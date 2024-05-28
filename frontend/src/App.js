import Player from "./components/Player";
import {useState} from "react";

function App() {
    const [songs, setSongs] = useState([
        {
            'id': '1',
            'title': 'idk',
        },
        {
            'id': '2',
            'title': 'idk2',
        }
    ])
    const [currentSongIndex, setCurrentSongIndex] = useState(0);

    return (
        <div className="App">
            <Player
                songs={songs}
                currentSongIndex={currentSongIndex}
                setCurrentSongIndex={setCurrentSongIndex}
            />
        </div>
    );
}

export default App;
