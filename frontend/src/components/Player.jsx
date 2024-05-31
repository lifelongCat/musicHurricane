import React, {useState, useEffect, useRef} from 'react';
import PlayerControls from "./PlayerControls";
import PlayerDetails from "./PlayerDetails";

function Player({songs, currentSongIndex, setCurrentSongIndex}) {
    const audioElement = useRef(null);
    const [isPlaying, setIsPlaying] = useState(false)

    useEffect(() => {
        if (isPlaying) {
            audioElement.current.play();
        } else {
            audioElement.current.pause();
        }
    }, [isPlaying]);

    const skipSong = (forwards = true) => {
        if (forwards) {
            setCurrentSongIndex(() => {
                let index = currentSongIndex;
                return ++index > (songs.length - 1) ? 0 : index
            });
        } else {
            setCurrentSongIndex(() => {
                let index = currentSongIndex;
                return --index < 0 ? (songs.length - 1) : index
            });
        }
    };

    return (
        <div>
            <audio
                src={`http://localhost:${process.env.REACT_APP_MINIO_PORT}/songs/${songs[currentSongIndex].id}`}
                ref={audioElement}>
            </audio>
            <PlayerDetails
                song={songs[currentSongIndex]}
            />
            <PlayerControls
                isPlaying={isPlaying}
                setIsPlaying={setIsPlaying}
                skipSong={skipSong}
            />
        </div>
    );
}

export default Player;
