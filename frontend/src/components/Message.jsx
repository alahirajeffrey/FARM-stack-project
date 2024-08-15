import PropTypes from "prop-types";

const PopUpMessage = ({ title, message }) => {
  return (
    <div className="fixed inset-0 flex items-center justify-center bg-blue-100 bg-opacity-50 z-50">
      <div className="bg-blue-800 p-6 rounded-lg text-white w-80 max-w-full">
        <h2 className="text-center font-bold text-gray-100 mb-4">{title}</h2>
        <p className="text-center text-gray-300">{message}</p>
      </div>
    </div>
  );
};

PopUpMessage.propTypes = {
  title: PropTypes.string.isRequired,
  message: PropTypes.string.isRequired,
};

export default PopUpMessage;
