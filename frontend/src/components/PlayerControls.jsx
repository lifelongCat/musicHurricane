import React from 'react';

function PlayerControls(props) {
    return (
        <div>
            <button onClick={() => props.skipSong(false)}>
                Назад
            </button>
            <button onClick={() => props.setIsPlaying(!props.isPlaying)}>
                {props.isPlaying ? 'Пауза' : 'Возобновить'}
            </button>
            <button onClick={() => props.skipSong()}>
                Вперёд
            </button>
        </div>
    );
}

export default PlayerControls;
