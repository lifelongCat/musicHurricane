import React, {useState, useEffect, useRef} from 'react';
import PlayerControls from "./PlayerControls";
import PlayerDetails from "./PlayerDetails";

function Player(props) {
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
            props.setCurrentSongIndex(() => {
                let index = props.currentSongIndex;
                return ++index > (props.songs.length - 1) ? 0 : index
            });
        } else {
            props.setCurrentSongIndex(() => {
                let index = props.currentSongIndex;
                return --index < 0 ? (props.songs.length - 1) : index
            });
        }
    };

    return (
        <div>
            <audio
                src={`http://localhost:8080/api/download/${props.songs[props.currentSongIndex].id}/`}
                ref={audioElement}>
            </audio>
            <PlayerDetails
                song={props.songs[props.currentSongIndex]}
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
