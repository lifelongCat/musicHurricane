import Player from "./components/Player";
import {useState, useEffect} from "react";

function App() {
    const [songs, setSongs] = useState([])
    const [currentSongIndex, setCurrentSongIndex] = useState(0);

    async function fetchSongs() {
        const response = await fetch('http://localhost:8080/api/compositions/');
        setSongs(await response.json());
    }

    useEffect(() => {
        fetchSongs();
    }, []);

    return !songs.length ?
        <h1>Загрузка плеера</h1> :
        (
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
