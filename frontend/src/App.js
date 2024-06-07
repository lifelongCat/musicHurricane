import Player from "./components/Player";
import {useState, useEffect} from "react";
import CompositionService from "./API/CompositionService";

function App() {
    const [songs, setSongs] = useState([])
    const [currentSongIndex, setCurrentSongIndex] = useState(0);

    async function fetchSongs() {
        const response = await CompositionService.getAll();
        setSongs(response.data);
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
