import Player from "./components/Player";
import {useState, useEffect} from "react";
import CompositionService from "./API/CompositionService";

function App() {
    const [songs, setSongs] = useState([])
    const [isCompositionsLoading, setCompositionsLoading] = useState(true);
    const [currentSongIndex, setCurrentSongIndex] = useState(0);

    async function fetchSongs() {
        const response = await CompositionService.getAll();
        setSongs(response.data);
        setCompositionsLoading(false);
    }

    useEffect(() => {
        fetchSongs();
    }, []);

    return (
        <div className="App">
            {isCompositionsLoading
                ? <h1>Загрузка плеера</h1>
                : !songs.length
                    ? <h1>Нет ни одного произведения</h1>
                    : <Player
                        songs={songs}
                        currentSongIndex={currentSongIndex}
                        setCurrentSongIndex={setCurrentSongIndex}
                    />
            }
        </div>
    );
}

export default App;
