import PropTypes from "prop-types";

const Button = ({ title, onClick }) => {
  return (
    <div>
      <button
        className="font-black text-bg bg-blue-400 rounded-lg px-2 py-2"
        onClick={onClick}
      >
        {title}
      </button>
    </div>
  );
};

Button.propTypes = {
  title: PropTypes.string.isRequired,
  onClick: PropTypes.func.isRequired,
};

export default Button;
